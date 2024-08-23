from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import nest_asyncio
import json


nest_asyncio.apply()

graph_config = {
   "llm": {
      "model": "ollama/llama3",
      "temperature": 1,
      "format": "json", 
      "model_tokens": 2000, 
      "base_url": "http://localhost:11434", 
   },
   "embeddings": {
      "model": "ollama/nomic-embed-text",
      "temperature": 0,
      "base_url": "http://localhost:11434",  
   },
   "verbose" : True
}

smart_scraper_graph = SmartScraperGraph(
   prompt="List me all the current Job listings and their descriptions.",\
   source="https://www.jobstreet.com.my/engineer-jobs",
   config=graph_config
)

result = smart_scraper_graph.run()
result = json.dumps(result,indent=2)
segments = result.split("\n")

for segment in segments:
    print(segment)


#TO DO
#Add Pagination
#Add Data pipeline