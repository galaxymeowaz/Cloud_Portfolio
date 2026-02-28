# ==============================================================================
# Automatic Accountant - Lambda Environment
# Created by AzTay (aztay.org) | Copyright (c) 2026
# Licensed under the MIT License. 
# ==============================================================================
# 1. Use the official AWS Lambda Python image (Required for AWS execution)
FROM public.ecr.aws/lambda/python:3.9

# 2. Copy dependencies if required
COPY requirements.txt ./
RUN pip install -r requirements.txt || true

# 3. Copy your local Python scripts into the container's designated task root
COPY calendar_sync.py ${LAMBDA_TASK_ROOT}

# 4. Point to the handler function inside your Python file (filename.function_name)
CMD ["calendar_sync.lambda_handler"]