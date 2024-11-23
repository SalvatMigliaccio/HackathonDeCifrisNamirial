from OpenSSL import crypto
import json


class KeyBundle(crypto.PKey):

    def __init__(self, private: dict = None, public: dict = None):
        super().__init__()
        if private and public:
            self.private = Private(**private)
            self.public = Public(**public)
        else:
            self.generate_key(crypto.TYPE_RSA, 1024)
            key_pair = self.to_cryptography_key()
            self.public = key_pair.public_key().public_numbers()
            self.private = key_pair.private_numbers()

    def download_keys(self, path: str = ".", output: str = None):
        public_key = {
            "e": self.e,
            "n": self.n,
        }

        private_key = {"d": self.d, "p": self.p, "q": self.q, "n": self.n, "e": self.e}

        with open(f"{path}\\{output}private.json", "w") as f:
            f.write(json.dumps(private_key))

        with open(f"{path}\\{output}public.json", "w") as f:
            f.write(json.dumps(public_key))

    @staticmethod
    def upload_key(path: str = ".", private: bool = False):
        with open(path) as f:
            return json.loads(f.read())

    @property
    def e(self):
        if type(self.public) == dict:
            return self.public.get("e")
        return self.public.e

    @property
    def n(self):
        if type(self.public) == dict:
            return self.public.get("n")
        return self.public.n

    @property
    def d(self):
        if type(self.private) == dict:
            return self.private.get("d")
        return self.private.d

    @property
    def p(self):
        if type(self.private) == dict:
            return self.private.get("p")
        return self.private.p

    @property
    def q(self):
        if type(self.private) == dict:
            return self.private.get("q")
        return self.private.q


class Public:
    def __init__(self, e, n):
        self.e = e
        self.n = n


class Private(Public):
    def __init__(self, d, p, q, e, n):
        super().__init__(e, n)
        self.d = d
        self.p = p
        self.q = q
