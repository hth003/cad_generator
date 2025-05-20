from firecrawl import FirecrawlApp, ScrapeOptions
import json
import os
from datetime import datetime
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)

def dump_json(data):
    """Convert data to JSON string with proper formatting"""
    return json.dumps(data, indent=2, cls=DateTimeEncoder)

def save_file(filepath, content):
    """Save content to a file"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def perform_web_crawl_and_save(url, file_crawl, file_map):
    """
    Crawl websites data and save to output json files

    :param url: url to crawl
    :param file_crawl: path to crawl result file
    :param file_map: path to map result file
    :return: n/a
    """
    app = FirecrawlApp(os.getenv("FIRECRAWL_API_KEY"))
    
    # Crawl the input url
    crawl_result = app.crawl_url(
        url,
        scrape_options=ScrapeOptions(formats=['markdown'])
    )
    map_result = app.map_url(url)
    
    # Save results to json files
    crawl_result_json = dump_json(crawl_result)
    save_file(file_crawl, crawl_result_json)
    print(f"Scrape result saved to {file_crawl}")

    map_result_json = dump_json(map_result)
    save_file(file_map, map_result_json)
    print(f"Map result saved to {file_map}")

def main():
    # Create output directory
    output_dir = os.path.join('knowledge', 'crawl_results')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filenames with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    crawl_file = os.path.join(output_dir, f'cadquery_docs_crawl_{timestamp}.json')
    map_file = os.path.join(output_dir, f'cadquery_docs_map_{timestamp}.json')
    
    # URL to crawl
    url = 'https://cadquery.readthedocs.io/'
    
    # Perform crawl and save results
    perform_web_crawl_and_save(url, crawl_file, map_file)

if __name__ == "__main__":
    main()
