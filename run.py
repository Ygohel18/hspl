import hspl

query = "indias cheap web hosting"
url = "hostingspell.com"

h = hspl.Hspl()
result = h.check(query, url)
print(result)
h.close_browser()
