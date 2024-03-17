import os
from fastapi import FastAPI, UploadFile
from typing import List
import nemo.collections.asr as nemo_asr
from dotenv import load_dotenv
import uvicorn


load_dotenv(".env")

app = FastAPI()
TEMP_DIRECTORY = './temp'

def save_uploaded_files(files: List[UploadFile]) -> List[str]:
    filenames = []
    for file in files:
        try:
            contents = file.file.read()
            os.makedirs(TEMP_DIRECTORY, exist_ok=True)
            uploaded_filename = os.path.join(TEMP_DIRECTORY, file.filename)
            with open(uploaded_filename, 'wb') as f:
                f.write(contents)
            filenames.append(uploaded_filename)
        except Exception as e:
            print(f"Error saving file: {e}")
    return filenames

def transcribe_files(filenames: List[str], asr_model) -> List[str]:
    hyps = asr_model.transcribe(filenames, batch_size=20)
    return hyps

@app.post("/transcript")
def transcribe_audio(files: List[UploadFile]):
    filenames = save_uploaded_files(files)
    transcriptions = transcribe_files(filenames, asr_model)
    for filename in filenames:
        os.remove(filename)
    return {
        "message": f"Successfuly uploaded {[file.filename for file in files]}",
        "result": [{"filename": filename, "transcription": transcription} for filename, transcription in zip(filenames, transcriptions)]
    }

if __name__ == '__main__':
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from(os.getenv('NEMO_MODEL_PATH'))
    uvicorn.run(app, host="127.0.0.1", port=8000)
