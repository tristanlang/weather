# original source: https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/quality-controlled-local-climatological-data-qclcd/qclcd-samples
# docs: http://www1.ncdc.noaa.gov/pub/data/normals/1981-2010/readme.txt
# home data dir: ftp://ftp.ncdc.noaa.gov/pub/data/normals/1981-2010/products/
# data dir to use: ftp://ftp.ncdc.noaa.gov/pub/data/normals/1981-2010/products/hourly/
# station names: ftp://ftp.ncdc.noaa.gov/pub/data/normals/1981-2010/station-inventories/allstations.txt
#
# dewp = dew point
# wind = wind speed
# temp = tempoeratur
#
# want 90th percentile and normal



#
# retrieve data from FTP
# http://stackoverflow.com/questions/18772703/read-a-file-in-buffer-from-ftp-python
#

from ftplib import FTP
import gzip
import StringIO

ftp = FTP('ftp.ncdc.noaa.gov')
ftp.login() # Username: anonymous password: anonymous@

sio = StringIO.StringIO()
def handle_binary(more_data):
    sio.write(more_data)

resp = ftp.retrbinary("RETR /pub/data/ghcn/daily/by_year/1763.csv.gz", callback=handle_binary)
sio.seek(0) # Go back to the start
zippy = gzip.GzipFile(fileobj=sio)

uncompressed = zippy.read()
print uncompressed