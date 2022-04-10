aws cloudformation update-stack \
--stack-name registration \
--template-body file://infrastructure/aws-python-config.yml \
--parameters file://infrastructure/aws-python-param.json \
--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
--region=us-west-2
