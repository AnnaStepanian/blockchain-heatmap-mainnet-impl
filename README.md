# Bitcoin Node Crawler and Heatmap

A Python-based Bitcoin network crawler that discovers Bitcoin **Mainnet** nodes, collects their information, and visualizes them on an interactive world map heatmap.

## Features

- **Bitcoin P2P Protocol Implementation**: Implements Bitcoin protocol messages from scratch
- **Async Crawling**: Uses asyncio for concurrent connections (500+ nodes simultaneously)
- **IP Geolocation**: Automatically geolocates IP addresses to show nodes on a world map
- **Interactive Heatmap**: Creates interactive heatmaps showing node distribution worldwide
- **Static Frontend**: Frontend can be deployed as a static website

## Usage - Command Sequence

Follow these commands **in order** to set up and run the Bitcoin node crawler:

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Crawl Bitcoin nodes, get geolocation, store in database, update JSON
python3 main.py --max-nodes 1000 --create-heatmap

# Step 3: Update JSON file with ALL nodes from database (not just new ones)
python3 -m backend.update_json

# Step 4: Create/update index.html with heatmap visualization
python3 create_index.py

# Step 5: Start HTTP server on http://localhost:8000 (Ctrl+C to stop)
python3 start_live_map.py
```

## Alternative Commands

### Update JSON File Only (Without Crawling)
```bash
# Update JSON file from existing database
python3 -m backend.update_json
```

### Create Heatmap from Existing Database (Skip Crawling)
```bash
# Create heatmap from existing database data
python3 main.py --heatmap-only
```

### Kill Process Using Port 8000 (If Needed)
```bash
# Kill process using port 8000
lsof -ti :8000 | xargs kill -9
```

## Deployment

The `frontend/` directory can be deployed as a **static website** to any hosting service (GitHub Pages, Netlify, Vercel, etc.).

**No server-side code is needed** - just upload the `frontend/` folder contents. The map will work as long as all files (`index.html`, `map.js`, `styles.css`, `bitcoin_nodes.json`) are accessible via HTTP/HTTPS.

## Command Line Options

- `--max-nodes`: Maximum number of nodes to crawl (default: 1000)
- `--max-concurrent`: Maximum concurrent connections (default: 500)
- `--timeout`: Connection timeout in seconds (default: 10.0)
- `--no-geolocation`: Skip IP geolocation step
- `--create-heatmap`: Create heatmap visualization after crawling
- `--heatmap-only`: Only create heatmap from existing database

## Troubleshooting

**No nodes crawled**: Check your internet connection or try increasing `--timeout`

**Geolocation fails**: Free API has rate limits; increase `--geolocation-rate-limit`

**JSON file not updating**: Run `python3 -m backend.update_json` to manually update it

## License

This project is for educational purposes. Use responsibly and respect Bitcoin network resources.
