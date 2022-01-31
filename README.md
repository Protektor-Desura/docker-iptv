A collection of IPTV scripts to get Live TV over the internet.

[PlutoTV](https://www.PlutoTV.com/) is an American internet television service owned by ViacomCBS. Pluto is a free, advertiser-supported video on demand (AVOD) service.  Pluto TV as of March 2020 has deals with 170 content partners providing more than 250 channels and 100,000 unique hours worth of programming.

This is a simple project that scrapes the website and generates an M3U playlist every 8 hours along with a XMLTV object that is hosted over NGINX.

The XMLTV and M3U playlist can be directly imported to Emby or Plex. Or if you'd like a buffer you can also import them into xteve or tvheadend. 


## Docker
```
docker run \
	--name=docker-plutotv \
	-p 8000:8000 \
	-v </path/to/appdata/config>:/config \
	--restart unless-stopped \
	docker-iptv:latest
```

## Parameters
Container specific parameters passed at runtime. The format is `<external>:<internal>` (e.g. `-p 443:22` maps the container's port 22 to the host's port 443).

| Parameter | Function |
| -------- | -------- |
| -p 8000 | This is the port inside the container by default however, you can map the outside port to be the same as the inner port. (Default 8000)  |
| -v /config | The directory where the application will store configuration information. |
| -e USERNAME | The Username you wish to run as. (Optional) |
| -e GROUPNAME | The Groupname you wish to run as. (Optional) |
| -e PUID | The UID you wish to run and save files as. (Optional) |
| -e PGID | The GID you wish to run and save files as. (Optional) |
| -e LOG_LEVEL | The Python Logging log level for the PTV Scraper. (Default: ERROR) |
| -e PLUTO_USER_ID | Your Pluto User ID. (Default: None) |
## Application Setup

The basic index is available at `http://<ip>:<port>/`

This will build and allow you to point your M3U Tuner to `http://<ip>:<port>/PlutoTV.m3u`
and your XEPG tuner to `http://<ip>:port/PlutoTVGuide.xml`
