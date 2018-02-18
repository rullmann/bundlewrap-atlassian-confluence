svc_systemd = {
    'atlassian-confluence': {},
}

files = {
    '/etc/systemd/system/atlassian-confluence.service.d/environment.conf': {
        'content_type': 'mako',
        'mode': '0644',
        'source': 'systemd-environment.conf',
        'triggers': ['svc_systemd:atlassian-confluence:restart', 'action:systemd-daemon-reload'],
    },
    '/opt/confluence/bin/setenv.sh': {
        'content_type': 'mako',
        'mode': '0755',
        'source': 'setenv.sh',
        'triggers': ['svc_systemd:atlassian-confluence:restart'],
    },
    '/opt/confluence/conf/server.xml': {
        'content_type': 'mako',
        'mode': '0644',
        'source': 'server.xml',
        'triggers': ['svc_systemd:atlassian-confluence:restart'],
    },
    '/opt/confluence/webapps/jolokia.war': {
        'owner': 'confluence',
        'content_type': 'binary',
        'mode': '0644',
        'triggers': ['svc_systemd:atlassian-confluence:restart'],
    },
}

directories = {
    '/opt/confluence/webapps': {
        'mode': '0755',
        'owner': 'confluence',
    },
}
