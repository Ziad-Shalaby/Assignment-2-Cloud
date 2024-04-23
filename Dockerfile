FROM python
WORKDIR /script
COPY require.txt .
RUN pip install -r require.txt
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
COPY . /script
CMD ["python3", "script.py"]


