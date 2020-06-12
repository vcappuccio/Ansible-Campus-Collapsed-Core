class FilterModule(object):

    def filters(self):
        return {
            'cleanup_device_data': self.cleanup_device_data,
        }

    def cleanup_device_data(self, value):
        site = {}
        core = {}
        access = {}
        for each in value:
            if each["device_role"]["name"] == 'core':
                core['name'] = each['name']
                core['tenant'] = each['tenant']['slug']
                core['platform'] = each['platform']['name']
                core['serial'] = each['serial']
                core['site'] = each['site']['slug']
            elif each["device_role"]["name"] == 'switch-l2':
                access['name'] = each['name']
                access['tenant'] = each['tenant']['slug']
                access['platform'] = each['platform']['name']
                access['serial'] = each['serial']
                access['site'] = each['site']['slug']
            else:
                pass
        
        site['core'] = core
        site['access'] = access
        return site