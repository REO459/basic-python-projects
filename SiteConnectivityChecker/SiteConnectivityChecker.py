import urllib.request as urllib


def main(url):
    print("Checking connectivity   ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity check program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)
