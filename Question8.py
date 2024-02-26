tested_true_url = "https://www.google.com"
tested_false_url = "www.google.com"
def url_true(url):
    """

    :param url: The URL to be verified
    :return: TRUE if it is valid and FALSE if it is not
    """
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

print(url_true(tested_true_url))
print(url_true(tested_false_url))