## zap2xml 

### TV Guide

zap2it -z -Z <zipcode> 

```  
  -u <username>
  -p <password>
  -d <# of days> (default = $days)
  -n <# of no-cache days> (from end)   (default = $ncdays)
  -N <# of no-cache days> (from start) (default = $ncsdays)
  -B <no-cache day>
  -s <start day offset> (default = $start)
  -o <output xml filename> (default = "$outFile")
  -c <cacheDirectory> (default = "$cacheDir")
  -l <lang> (default = "$lang")
  -i <iconDirectory> (default = don't download channel icons)
  -m <#> = offset program times by # minutes (better to use TZ env var)
  -b = retain website channel order
  -x = output XTVD xml file format (default = XMLTV)
  -w = wait on exit (require keypress before exiting)
  -q = quiet (no status output)
  -r <# of connection retries before failure> (default = $retries, max 20)
  -e = hex encode entities (html special characters like accents)
  -E "amp apos quot lt gt" = selectively encode standard XML entities
  -F = output channel names first (rather than "number name")
  -O = use old tv_grab_na style channel ids (C###nnnn.zap2it.com)
  -A "new live" = append " *" to program titles that are "new" and/or "live"
  -M = copy movie_year to empty movie sub-title tags
  -U = UTF-8 encoding (default = "ISO-8859-1")
  -L = output "<live />" tag (not part of xmltv.dtd)
  -T = don't cache files containing programs with "$sTBA" titles 
  -P <http://proxyhost:port> = to use an http proxy
  -C <configuration file> (default = "$confFile")
  -S <#seconds> = sleep between requests to prevent flooding of server 
  -D = include details = 1 extra http request per program!
  -I = include icons (image URLs) - 1 extra http request per program!
  -J <xmltv> = include xmltv file in output
  -Y <lineupId> (if not using username/password)
  -Z <zipcode> (if not using username/password)
  -z = use tvguide.com instead of zap2it.com
  -a = output all channels (not just favorites) 
  -j = add "series" category to all non-movie programs
  ```
