# Name Entity Recognition for Medical Transcripts

Performing NER on MEdical Datasets

## Running the Project

### Creating the Environment

1. Install Pytorch

   Pytorch is a requirement for running some of the libraries. However, pytorch implementation varies according to machine, so it has to be done manually.

   Refer to <https://pytorch.org/get-started/locally/> for installation.

2. Installing requirements

    Requirements can be installed using `pip` as:

    ```shell
    pip install -r requirements.txt
    ```

    *Note: The dependencies are a bit large so a stable internet connection and a bit of patience is required*

3. Installing language model

   The project makes use of a Spacy model. We can download it by the command:

   ```shell
   python -m spacy download en_core_web_lg
   ```

### Running the Notebook

1. We need jupyter installed to run the notebook

    ```shell
    pip install jupyter
    ```

2. Launch the notebook interface using command

    ```shell
    jupyter notebook
    ```

3. Navigate to the required notebook in the notebooks directory to view.
    * `medical_ner.ipynb` depicts step by step, how medical NER is performed in this project.
    * `mongo-playground.ipynb` contains code for inserting the extracted records into MongoDB.
    * `stanza_playground.ipynb` contains experimental code with the `stanza` NLP library. 

### Running From CLI

We can run the NER data extractor from the cli too by using the command from the base dir.

```shell
python medical_ner.py <location-to-file>
```

For instance,

```shell
python medical_ner.py datasets/report_0.txt
```

### Running the Scraper
A web scraper was built to extract Medical Transcript samples from https://medical-transcription-sample-reports.blogspot.com/.

The scraper is placed in the scraper directory and can be run as:
```shell
python record_scraper.py
```

## Sample Output
![Output of NER extractor](/assets/ner-output.png)