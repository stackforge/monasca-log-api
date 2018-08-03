# Copyright 2018 OP5 AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from monasca_log_api.policies import AGENT_AUTHORIZED_ROLES
from monasca_log_api.policies import DEFAULT_AUTHORIZED_ROLES
from monasca_log_api.policies import DELEGATE_AUTHORIZED_ROLES


rules = [
    policy.DocumentedRuleDefault(
        name='log_api:logs:post',
        check_str=' or '.join(filter(None, [AGENT_AUTHORIZED_ROLES,
                                            DEFAULT_AUTHORIZED_ROLES,
                                            DELEGATE_AUTHORIZED_ROLES])),
        description='Logs post rule',
        operations=[
            {'path': '/logs', 'method': 'POST'},
            {'path': '/log/single', 'method': 'POST'}
        ]
    )
]


def list_rules():
    return rules