## Setup

1. conda pytorch setup
    ```
    $ conda create --name venv python=3.9
    $ conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 -c pytorch
    ```

2. venv activate
    - To activate this environment, use
    ```
    $ conda activate venv
    ```
    - To deactivate an active environment, use
    ```
    $ conda deactivate
    ```

3. whisper install
    ```
    $ pip install git+https://github.com/openai/whisper.git 
    ```

### Reference
- https://openai.com/blog/whisper/
- https://github.com/openai/whisper/
