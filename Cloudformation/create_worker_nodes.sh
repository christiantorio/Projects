aws cloudformation create-stack --stack-name registration-worker-nodes --template-body file://infrastructure/worker_nodes.yml --parameters file://infrastructure/worker_nodes_parameters.json --capabilities CAPABILITY_IAM
