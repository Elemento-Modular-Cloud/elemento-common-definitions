# Accepted values for supported providers file
Example with accepted values for a single provider:
```json
{
    "ELEMENTO_SUPPORTED_PROVIDERS": {
        "provider_name": {
            "display_name": "string",
            "icon_classes": "<provider_name>_icon",
            "source": "fontawesome",
            "hex_color": "#4285f4",
            "svg_filename": "<provider_name>_icon.svg",
            "status": "soon|development|beta|production",
            "server_ips": [],  // List of IPs for the active provider's mesons
            "services": [
                {
                    "name": "string",
                    "display_name": "string",
                    "type": "compute|storage|network|service",
                    "sub_type": "vm|objectstorage|k8s|...",
                    "regions": {
                        "africa_south1": {
                            "country": "South Africa",
                            "location": "Johannesburg",
                            "plus_code": "",
                            "certifications": []
                        },
                        "asia_east1": {
                            "country": "Taiwan",
                            "location": "Changhua County",
                            "plus_code": "",
                            "certifications": []
                        },
                        "asia_east2": {
                            "country": "China",
                            "location": "Hong Kong",
                            "plus_code": "",
                            "certifications": []
                        },
                        {
                            "Other regions": "..."
                        }
                    },
                    "support_level": "planned|partial|full" 
                },
                {
                    "Other services": "..."
                }
            ]
        },
    }
}
```
# Supported Providers

This document lists all supported cloud providers and their services.



















<!-- PROVIDERS_TABLE_START -->

| Provider | Service | Type | Sub-Type | Support Level | Status |
|----------|---------|------|----------|----------------|--------|
| Azure | Block Storage | storage | blockstorage | full | production |
| Azure | Caddy CA Issuer | service | caddy_ca | full | production |
| Azure | Hermes Agent | service | hermes | full | production |
| Azure | Hosting | service | hosting | full | production |
| Azure | LiteLLM Proxy | service | litellm | full | production |
| Azure | LM Studio | service | llmstudio | full | production |
| Azure | MinIO | service | minio | full | production |
| Azure | n8n | service | n8n | full | production |
| Azure | n8n AI Sandbox Runner | service | n8n_runner | full | production |
| Azure | Nginx Proxy Manager | service | npm | full | production |
| Azure | Object Storage | storage | objectstorage | full | production |
| Azure | OpenClaw | service | openclaw | full | production |
| Azure | Open WebUI | service | openwebui | full | production |
| Azure | SearXNG | service | searxng | full | production |
| Azure | VM Management | compute | vm | dev | production |
| Google | Block Storage | storage | blockstorage | full | production |
| Google | Caddy CA Issuer | service | caddy_ca | full | production |
| Google | Database | service | dbaas | full | production |
| Google | Hermes Agent | service | hermes | full | production |
| Google | Hosting | service | hosting | full | production |
| Google | Kubernetes | service | kaas | full | production |
| Google | LiteLLM Proxy | service | litellm | full | production |
| Google | LM Studio | service | llmstudio | full | production |
| Google | MinIO | service | minio | full | production |
| Google | n8n | service | n8n | full | production |
| Google | n8n AI Sandbox Runner | service | n8n_runner | full | production |
| Google | Nginx Proxy Manager | service | npm | full | production |
| Google | OpenClaw | service | openclaw | dev | production |
| Google | Open WebUI | service | openwebui | full | production |
| Google | SearXNG | service | searxng | full | production |
| Google | VM Management | compute | vm | full | production |
| Impossible Cloud | Object Storage | service | objectstorage | full | production |
| OVH | Kubernetes | service | kaas | full | production |
| OVH | VM Management | matcher | vm | dev | production |
| Scaleway | Kubernetes | service | kaas | full | production |
| Scaleway | Object Storage | storage | objectstorage | full | production |
| UpCloud | Block Storage | storage | blockstorage | full | production |
| UpCloud | Caddy CA Issuer | service | caddy_ca | full | production |
| UpCloud | Database as a Service | service | dbaas | full | production |
| UpCloud | Hermes Agent | service | hermes | full | production |
| UpCloud | Hosting | service | hosting | full | production |
| UpCloud | Kubernetes | service | kaas | full | production |
| UpCloud | LiteLLM Proxy | service | litellm | full | production |
| UpCloud | LM Studio | service | llmstudio | full | production |
| UpCloud | MinIO | service | minio | full | production |
| UpCloud | n8n | service | n8n | full | production |
| UpCloud | n8n AI Sandbox Runner | service | n8n_runner | full | production |
| UpCloud | Nginx Proxy Manager | service | npm | full | production |
| UpCloud | Object Storage | storage | objectstorage | full | production |
| UpCloud | OpenClaw | service | openclaw | full | production |
| UpCloud | Open WebUI | service | openwebui | full | production |
| UpCloud | SearXNG | service | searxng | full | production |
| UpCloud | VM Management | matcher | vm | dev | production |
| Wasabi | Object Storage | storage | objectstorage | full | production |

