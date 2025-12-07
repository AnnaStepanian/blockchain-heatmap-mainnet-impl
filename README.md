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

### Step 1: Install Dependencies
```bash
# Install all required Python packages (asyncio, aiohttp, etc.)
pip install -r requirements.txt
```

### Step 2: Crawl Bitcoin Nodes
```bash
# Crawl Bitcoin network, discover nodes, get geolocation data, and store in database
# This will:
#   - Connect to seed nodes and discover other Bitcoin nodes
#   - Collect node information (IP, port, version, etc.)
#   - Get geolocation data for each IP address
#   - Store all data in SQLite database (backend/bitcoin_nodes.db)
#   - Update frontend/bitcoin_nodes.json with newly crawled nodes
python3 main.py --max-nodes 1000 --create-heatmap
```

### Step 3: Update JSON File (Optional but Recommended)
```bash
# Update frontend/bitcoin_nodes.json with ALL nodes from database (not just new ones)
# This ensures the JSON file contains all historical nodes, not just the ones from the last crawl
python3 -m backend.update_json
```

### Step 4: Create/Update Index HTML (Optional)
```bash
# Create or update the frontend/index.html file with heatmap visualization
# This generates the HTML file that displays the interactive map
python3 create_index.py
```

### Step 5: Start the Web Server
```bash
# Start HTTP server on http://localhost:8000 and open the map in your browser
# The server serves the frontend files (index.html, map.js, styles.css, bitcoin_nodes.json)
# Press Ctrl+C to stop the server
python3 start_live_map.py
```

## Alternative Commands

### Update JSON File Only (Without Crawling)
```bash
# If you already have nodes in the database and just want to update the JSON file
python3 -m backend.update_json
```

### Create Heatmap from Existing Database (Skip Crawling)
```bash
# If you already have node data in the database and want to create/update the heatmap
python3 main.py --heatmap-only
```

### Kill Process Using Port 8000 (If Needed)
```bash
# If port 8000 is already in use, kill the process using it
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
