Pipeline to count skills in my job_skills.csv:
cut -d , -f 4 job_skills.csv | tail -n +2 | sort | uniq -c | sort -n -r

Output:
    4 Python
      2 machine learning
      2 large language models
      2 communication
      1 statistics
      1 startup experience
      1 spaCy
      1 pytest
      1 natural language processing
      1 model parallelism
      1 geometric deep learning
      1 generative AI (transformers/GANs/VAEs)
      1 deep learning
      1 data structures and algorithms
      1 SageMaker
      1 PyTorch
      1 MLOps
      1 LLM APIs (open-source or commercial)
      1 HuggingFace
      1 AWS

Command to check for ^M windows carraige return
grep -c $'\r' job_skills.csv
Output:0
tested with line.txt where there are 4 carraige returns
grep -c $'\r' line.txt
Output:4