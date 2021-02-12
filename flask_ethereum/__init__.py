from jinja2 import Markup
from flask import current_app


class _web3:

    @staticmethod
    def include_web3():
        return Markup(f'''
            <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
            <script>
            import Web3 from "web3";
            import Web3Connect from "web3connect";

            const web3Connect = new Web3Connect.Core({
                network: "mainnet",
                cacheProvider: true,
            });
            const provider = await web3Connect.connect();
            window.web3 = new Web3(provider);

            var addresses = document.getElementsByClassName("web3_address");
            Array.prototype.forEach.call(addresses, function(address, index) {
                address.innerHTML = window.web3.eth.accounts[0];
            });
            </script>
        ''')

    @staticmethod
    def user_address():
        # NOTE This will get replaced on the client side with the user's address
        return Markup('<span class="web3_address">0x0000000000000000000000000000000000000000</span>')


class Web3:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['web3'] = _web3
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {
            'web3': current_app.extensions['web3']
        }

    def __getattr__(self, name):
        return getattr(current_app.extensions['web3'], name)
