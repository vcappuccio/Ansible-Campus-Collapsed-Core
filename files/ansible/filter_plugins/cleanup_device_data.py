class FilterModule(object):

    def filters(self):
        return {
            'cleanup_device_data': self.cleanup_device_data,
        }

    def cleanup_device_data(self, value):
        site = {}
        cpe = {}
        switch = {}
        for each in value:
            if each["device_role"]["name"] == 'sdwan-cpe':
                cpe['name'] = each['name']
                cpe['tenant'] = each['tenant']['slug']
                cpe['platform'] = each['platform']['name']
                cpe['serial'] = each['serial']
                cpe['site'] = each['site']['slug']
            elif each["device_role"]["name"] == 'switch-l2':
                switch['name'] = each['name']
                switch['tenant'] = each['tenant']['slug']
                switch['platform'] = each['platform']['name']
                switch['serial'] = each['serial']
                switch['site'] = each['site']['slug']
            else:
                pass
        
        site['cpe'] = cpe
        site['switch'] = switch
        return site