from os import path

import predict_molec_prop

base_path = path.dirname(path.dirname(predict_molec_prop.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
