from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import nest_asyncio
import json
import csv

nest_asyncio.apply()

# Read CSV and flatten the list
with open('TestSheetURL - Sheet5 (2).csv', newline='') as f:
    reader = csv.reader(f)
    sources = [row[0] for row in reader if row]  # Take the first column and ignore empty rows

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

results = []
for source in sources:
    try:
        smart_scraper_graph = SmartScraperGraph(
            prompt="List me the company name and its details.",
            source=source, 
            config=graph_config
        )
        result = smart_scraper_graph.run()
        result_json = json.dumps(result, indent=2)
        print(result_json)
        results.append(result_json)
    except Exception as e:
        print(f"Error processing source {source}: {str(e)}")

all_segments = []
for result in results:
    segments = result.split("\n")
    all_segments.extend(segments)

for segment in all_segments:
    print(segment)

# TO DO
# Add Data pipeline to clean data