# Bitcoin Node Crawler and Heatmap

A Python-based Bitcoin network crawler that discovers Bitcoin **Mainnet** nodes, collects their information, and visualizes them on an interactive world map heatmap.

## Features

- **Bitcoin P2P Protocol Implementation**: Implements Bitcoin protocol messages from scratch
- **Async Crawling**: Uses asyncio for concurrent connections (500+ nodes simultaneously)
- **IP Geolocation**: Automatically geolocates IP addresses to show nodes on a world map
- **Interactive Heatmap**: Creates interactive heatmaps showing node distribution worldwide
- **Static Frontend**: Frontend can be deployed as a static website

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

### View the Map

Start the HTTP server to view the map:

```bash
python3 start_live_map.py
```

This will start a server on `http://localhost:8000` and open the map in your browser. The map displays a snapshot of nodes from `bitcoin_nodes.json`.

### Crawl Nodes and Create Heatmap

Crawl Bitcoin Mainnet nodes and create a heatmap:

```bash
python3 main.py --max-nodes 1000 --create-heatmap
```

This will:
1. Crawl up to 1000 nodes
2. Get geolocation data
3. Store data in the database
4. Generate the interactive heatmap

### Update Node Data

To update the `bitcoin_nodes.json` file from the database:

```bash
python3 -m backend.update_json
```

The map displays a snapshot - update the JSON file manually to refresh the data.

### View Existing Data

If you already have node data in the database:

```bash
python3 main.py --heatmap-only
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
