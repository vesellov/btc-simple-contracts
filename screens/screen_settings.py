from kivy.app import App
from kivy.properties import ObjectProperty  # @UnresolvedImport

#------------------------------------------------------------------------------

from components.screen import AppScreen
from storage import local_storage

#------------------------------------------------------------------------------

kv = """
<OptionHeaderLabel@Label>:
    size_hint_x: None
    size_hint_y: None
    width: dp(260)
    height: dp(50)
    valign: 'bottom'
    halign: 'right'
    pos_hint: {'right': 1}
    text_size: self.size
    font_size: 18
    

<OptionFieldLabel@Label>:
    size_hint_x: None
    size_hint_y: None
    width: dp(260)
    height: dp(30)
    pos_hint: {'right': 1}
    valign: 'middle'
    halign: 'right'
    text_size: self.size


<OptionFieldInput@TextInput>:
    size_hint_x: None
    size_hint_y: None
    width: dp(360)
    height: self.minimum_height
    multiline: False


<SettingsScreen>:

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1

        ScrollView:
            bar_width: 15
            bar_color: .2,.5,.8,1
            bar_inactive_color: .1,.4,.7,1
            effect_cls: "ScrollEffect"
            scroll_type: ['bars']

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, None
                height: self.minimum_height

                Widget:
                    size: 1, 1
                    size_hint: 0.5, 1

                GridLayout:
                    size_hint_x: None
                    size_hint_y: None
                    width: self.minimum_width
                    height: self.minimum_height
                    pos_hint: {'center_x': 0.5, 'top': 1}
                    cols: 2
                    padding: 10
                    spacing: 10
    
                    OptionHeaderLabel:
                        text: "company business details"
                    Widget:
                        size: 1, 1
    
                    OptionFieldLabel:
                        text: "company name:"
                    OptionFieldInput:
                        id: business_company_name
                        text: ""
                        on_text: root.on_field_modified('business_company_name')
    
                    OptionFieldLabel:
                        text: "owner first name:"
                    OptionFieldInput:
                        id: business_owner_first_name
                        text: ""
                        on_text: root.on_field_modified('business_owner_first_name')
    
                    OptionFieldLabel:
                        text: "owner last name:"
                    OptionFieldInput:
                        id: business_owner_last_name
                        text: ""
                        on_text: root.on_field_modified('business_owner_last_name')

                    OptionFieldLabel:
                        text: "address:"
                    OptionFieldInput:
                        id: business_address
                        text: ""
                        on_text: root.on_field_modified('business_address')

                    OptionFieldLabel:
                        text: "email:"
                    OptionFieldInput:
                        id: business_email
                        text: ""
                        on_text: root.on_field_modified('business_email')

                    OptionFieldLabel:
                        text: "phone number:"
                    OptionFieldInput:
                        id: business_phone
                        text: ""
                        on_text: root.on_field_modified('business_phone')

                    OptionFieldLabel:
                        text: "BitCoin address:"
                    OptionFieldInput:
                        id: receiving_btc_address
                        text: ""
                        on_text: root.on_field_modified('receiving_btc_address')

                    OptionHeaderLabel:
                        text: "access to live BTC/USD prices"
                    Widget:
                        size: 1, 1
    
                    OptionFieldLabel:
                        text: "CoinMarketCap API key:"
                    OptionFieldInput:
                        id: coinmarketcap_api_key
                        text: ""
                        on_text: root.on_field_modified('coinmarketcap_api_key')

                Widget:
                    size: 1, 1
                    size_hint: 0.5, 1

        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            padding: 10
            spacing: 2

            RoundedButton:
                id: save_settings_button
                size_hint_x: None
                width: 120
                text: ' save '
                disabled: True
                on_release: root.on_save_button_clicked()

"""

#------------------------------------------------------------------------------

class SettingsScreen(AppScreen):

    def populate(self, *args):
        cur_settings = local_storage.read_settings()
        self.ids.business_company_name.text = cur_settings.get('business_company_name', '')
        self.ids.business_owner_first_name.text = cur_settings.get('business_owner_first_name', '')
        self.ids.business_owner_last_name.text = cur_settings.get('business_owner_last_name', '')
        self.ids.business_address.text = cur_settings.get('business_address', '')
        self.ids.business_email.text = cur_settings.get('business_email', '')
        self.ids.business_phone.text = cur_settings.get('business_phone', '')
        self.ids.receiving_btc_address.text = cur_settings.get('receiving_btc_address', '')
        self.ids.coinmarketcap_api_key.text = cur_settings.get('coinmarketcap_api_key', '')
        self.ids.save_settings_button.disabled = True

    def on_enter(self, *args):
        self.populate()

    def on_field_modified(self, field_name):
        self.ids.save_settings_button.disabled = False

    def on_save_button_clicked(self, *args):
        cur_settings = local_storage.read_settings()
        cur_settings['receiving_btc_address'] = self.ids.receiving_btc_address.text
        cur_settings['coinmarketcap_api_key'] = self.ids.coinmarketcap_api_key.text
        cur_settings['business_company_name'] = self.ids.business_company_name.text
        cur_settings['business_owner_first_name'] = self.ids.business_owner_first_name.text
        cur_settings['business_owner_last_name'] = self.ids.business_owner_last_name.text
        cur_settings['business_address'] = self.ids.business_address.text
        cur_settings['business_email'] = self.ids.business_email.text
        cur_settings['business_phone'] = self.ids.business_phone.text
        local_storage.write_settings(cur_settings)
        self.ids.save_settings_button.disabled = True
