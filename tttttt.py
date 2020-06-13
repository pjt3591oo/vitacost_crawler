import requests as rq
from bs4 import BeautifulSoup

url = "https://www.vitacost.com/magnesium-50?mp=1&pg=2"

# 해당 값이 없으면 timeout 발생
# cookie가 없으면 상품의 품절 여부인 Detail 텍스트가 아닌 Add to chart만 출력됨
headers = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
  'cookie': 'vitaguid=7d66983f-001b-48a2-a795-6540542af78a; CtGUID=0415a341-5509-4a76-95bc-63f909e1d53e; FirstPartyCookie=True; GuestCustTransit=Zip=&Country=109; _sdsat_Customer Segment=; _fbp=fb.1.1591661443933.1587003963; s_ecid=MCMID%7C85973490785519529511577933545079449455; vcemailtop=true; _abck=B9B62A5E0CC78651FC4F7FF3F6F70F03~0~YAAQRzVDF2U/OJNyAQAAUEBqlgT6SWEIuOvNScCQeJIJosTXxaEu9Oo0I+qN9YzZ9Ig5lqvDlnAN7LHuuRv0PDV7Lna4Xs0SEy61S6SinZPooh+LLegmbIZ8J6DiMbXWiLRH/BCK9mNgkxqwpkeSll6g23AyNWZenIrrAvpQj5cdrty0BVU0PpU+KvHASHOHnJQXmIVH9avRPOe5bKcP+KtnChUI+goriojmFzvWw2/tn3gsVs572lcVfVmGQeUj3CHHDd33gzSM8ew6vZOjcrkoxAukNrzmEh/4lf5JUzOvrxOYMNmPvW2vQMO4QP0ZYSZ05WdSxqGX~-1~-1~-1; __gads=ID=8ab0bf6fdc1fd327:T=1591661444:S=ALNI_MZX_P36ZV4f8PmJJl4P9A37hrhDvw; _gcl_au=1.1.1450074016.1591661446; sbt_i=7ZGI1ZGU5NDYtMTU2NC00YjE0LWIwNDktNGZkZGI3OGUyNGU5OzNmJhMWRlMzYtOTY5OC00ZmNhLTljNWItNjc0YTM3ZWRlMmM2OzsA=; th_u=j%26%23BXO7qaVk~%26xuNCm%238; th_v=j%26%23BXO7qaVk~%26xuNCm%238; ASP.NET_SessionId=jm2nq04bfldcri5gbrmrfbqa; origin=lvdc; IsNewUser=False; __Sally=d77a5c583e52423f85f03989b139f1cf; useAjaxForCartRefresh=true; akaalb_Vitacost_ALB=~op=VC_vitacost:lvdc|~rv=27~m=lvdc:0|~os=d28d1bedc64938865acbb3d9b52a5c3b~id=bd66027d7e1c537b0b821ff42e6f71a4; bm_sz=D59C3AD27ACA22BB5D8A9BD58FB75F49~YAAQRzVDF3yY3qdyAQAAxbKyqggBHPcisIKEmgV0mzk/817gsH2fXTjDq5VWS1TKP93ldbNjiDiOg5j5kDdYni/6J0fwcDVh18AaYiYNPCr0oy0D+4QBksfxsG1GK4W2v5uI4WSjG5QNADah5cDyed4ujx5j6bqV8QCA30DH/+XZpKEVoiVOEdkImJYwfwwiz2A=; check=true; AMCVS_A88E776A5245B3F40A490D44%40AdobeOrg=1; AMCV_A88E776A5245B3F40A490D44%40AdobeOrg=-1712354808%7CMCIDTS%7C18426%7CMCMID%7C85973490785519529511577933545079449455%7CMCAAMLH-1592606538%7C11%7CMCAAMB-1592606538%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1592008938s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; ak_bmsc=CC2451E5F0D13A05367DD681FEB9115417433547815A0000C904E45E96F07761~plGxSe7ZKzbpTdgBAup0eWgMh6r51DJ+oZ79JQCZ7IgJNBdy/WQD1jN5Off0/Rd0XLZ5Rki6DkQm39hiyvoYWbl9zpfQR7nd2R/tZUsLYf5+lwvrKtzYL8FmKeOoMKsKYeyhU9GzX1kOD6GN9WjO25UCumHIBXppuxMnWQQS53EWsirbk0H/gedwwdj5OoZ/+bZ/F4NSrfSOGIHAyw2skExVx5in2TdC/RlUGaSWa5al0F7G45Ie/nk9E5ED9h6ijQ; s_cc=true; _hjid=e0152a20-97f8-403a-9b0b-7e1a73a7aae5; productcomparison=null; s_sq=%5B%5BB%5D%5D; TS014a96aa_77=08abb0bc28ab2800ebad14fc9c57ffaebe1acfbe328189eeb5f10c4266718d591a1a043d16814cec8d2805bf24e893da0855cd47a2823800a20cf78e31dc6f3c6f6092d329b0ac247f55180525321679039e86e28b9ee3064061c1d4bfd5ac46bf4d9d4fc933bdf355ad324d80f8226e; _hjIncludedInSample=1; TS014a96aa=01bd4ca7ce0110a4e537e4680b4a6e555024e1ccc45d63cb32d1979130e4887109fecd678ed6308565be627fa25f004805339ea051cba444e5114aa81baab1bea07cb4ea8311df711162cd6dbcd38a908935cf3e6ae6a43ca569da44ef89d5df225bc8d64e396939275b8ad1bc8880af35d2c2195e51f1e0d857d4b22cf51703fda932b63f7d25cd865d612013380b815e065a1652fbf2f9b8f7af91db1158cea7150dc6a8c0ac8f2a649dbe7e7e64164f1984da37083d181cbd674c66517f58aa440ddfa7; mbox=PC#b684340d055b4834a179f270c005e880.32_0#1654906245|session#c4fc9bc7a7804df0acc67ea6c9180fd8#1592006728; _uetsid=75ee9c60-2814-fec6-ed8a-5867d784ee53; _uetvid=4174dd71-72d0-b878-35ec-a99d1d834772; f5avr1288675822aaaaaaaaaaaaaaaa=DJGOILJGJMNMANHJBGPOCLOHLEDPOHANNBMMFIHJIAAGGMJCPMACCJBLGACDNPFPBAGCLPEIMEEAELJDGFGAAMPOBAODJOAIGDMEPNJHHOMNKGJIAHIICLHAMKDJKJID; bm_sv=1560BA7DF6250CCB73BB8DDEB667F7CD~yrakYAoNWwREZntPFlhfg6PdCM/5O6nTiObd7THcy8tBSeiIN1jAxF5QdKbTaq7wY3I4wix0cFhPdu9Gw61vO7XjcZd6jlKqoVaTwkYaU4AOWQjvQDlC9eCoHmye1iNWL8vpwwx3scHnY+t0zgrPBrwWVL9lXQxm7hbzD5UEcIw=; RT="sl=3&ss=1592004393881&tt=23007&obo=0&sh=1592004868077%3D3%3A0%3A23007%2C1592004848339%3D2%3A0%3A15835%2C1592004780043%3D1%3A0%3A8018&dm=vitacost.com&si=d605889d-8c39-456e-9d6e-c6c81f2d2641&bcn=%2F%2F684fc53f.akstat.io%2F&r=https%3A%2F%2Fwww.vitacost.com%2Fmagnesium-50%3Fmp%3D1%26pg%3D2&ul=1592006961760'
}
res = rq.get(url, headers=headers)

with open('origin.html', 'w') as f:
    f.write(str(res.text))
    
soup = BeautifulSoup(res.content, 'lxml')
items = soup.select('.productWrapper .product-block')

for idx, item in enumerate(items):
  print(idx)
  print(item.find('div', {"class": "pb-image"}).get('style'))
  print(item.find('div', {"class": "pb-lower"}).find('a', {"class": "button1"}).text)
  print()
  with open(str(idx)+'.html', 'w') as f:
    f.write(str(item))

  print()