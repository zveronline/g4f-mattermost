Mattermost chatgpt bot

Sample docker compose:

```
  gpt-bot:
    image: ghcr.io/zveronline/g4f-mattermost:latest
    hostname: "{{.Service.Name}}"
    deploy:
      mode: replicated
      replicas: 1
    volumes:
      - type: tmpfs
        target: /dev/shm
        tmpfs:
           size: 2096000000 # (this means 2GB)
      - /mnt/ceph/gpt4/har_and_cookies:/bot/har_and_cookies
      - /mnt/ceph/gpt4/generated_images:/bot/generated_images
```