import glob
from datetime import datetime
print('Collecting files...')
html = glob.glob('./' + '/**/*.html', recursive=True)
css = glob.glob('./' + '/**/*.css', recursive=True)
js = glob.glob('./' + '/**/*.js', recursive=True)
svg = glob.glob('./' + '/**/*.svg', recursive=True)
ico = glob.glob('./' + '/**/*.ico', recursive=True)
wav = glob.glob('./' + '/**/*.wav', recursive=True)
mp3 = glob.glob('./' + '/**/*.mp3', recursive=True)
# ogg = glob.glob('./' + '/**/*.ogg', recursive=True)
print('Writing...')
split = "',\n\t'"
text = "[\n\t'"+split.join(html)+split+split.join(css)+split+split.join(js)+split+split.join(svg)+split+split.join(ico)+split+split.join(wav)+split+split.join(mp3)+"'\n]"
print(text)
list = open('list.txt', 'w')
list.write(text)
list.close()
split = "',\n\t\t\t\t'"
text = "[\n\t\t\t\t'"+split.join(html)+split+split.join(css)+split+split.join(js)+split+split.join(svg)+split+split.join(ico)+split+split.join(wav)+split+split.join(mp3)+"'\n\t\t\t]"
sw = open('service-worker.js', 'w')
sw.write("""
/*
\t! when updating this file, update the template in `/list.py`.
\t$ the list of files to be cached comes from the script in `/list.py`.
\t$ this list can be updated manually by running `/list.py`.
*/
/*
\tThis comment was generated by `/list.py`.
\tTimestamp: """ + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + """
*/
self.addEventListener("install", (event) => {
\tevent.waitUntil(
\t\tcaches.open("lightblue").then((cache) => {
\t\t\tcache.addAll(""" + text + """);
\t\t})
\t);
});

self.addEventListener("fetch", (event) => {
\tevent.respondWith(
\t\tfetch(event.request).then((response) => {
\t\t\treturn response;
\t\t}).catch(async (error) => {
\t\t\treturn caches.match(event.request).then((cacheRes) => {
\t\t\t\treturn cacheRes;
\t\t\t});
\t\t})
\t);
});
""")
print('Done.')