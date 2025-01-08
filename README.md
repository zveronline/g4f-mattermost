#### Mattermost chatgpt bot

Sample docker compose:

```
  gpt-bot:
    image: ghcr.io/zveronline/g4f-mattermost:latest
    hostname: "{{.Service.Name}}"
    deploy:
      mode: replicated
      replicas: 1
    environment:
      - MM_URL="https://mattermost.example.com"
      - MM_TOKEN="12345"
      - MM_TEAM="superteam"
    volumes:
      - type: tmpfs
        target: /dev/shm
        tmpfs:
           size: 2096000000 # (this means 2GB)
      - /mnt/ceph/gpt4/har_and_cookies:/app/har_and_cookies
      - /mnt/ceph/gpt4/generated_images:/app/generated_images
```
