'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from radish import before, after


@before.each_scenario
def prepare_traversal_source(scenario):
    scenario.context.remote_conn_modern = DriverRemoteConnection('ws://localhost:45940/gremlin', 'g')


@after.each_scenario
def close_traversal_source(scenario):
    scenario.context.remote_conn_modern.close()
