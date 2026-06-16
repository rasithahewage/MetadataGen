import {storeAllToplevel} from "./selectFromFrameworks/frameworkManager.js";
import {buildGeneralUi} from "./inputFormTemplates/generalData.js";
import {buildLicenseUi} from "./inputFormTemplates/licenses.js";
import {buildPublisherUi} from "./inputFormTemplates/publisher.js";
import {buildCreatorUi} from "./inputFormTemplates/creator.js";
import {buildKeywordsUi} from "./inputFormTemplates/keywords.js";
import {buildBaseUi} from "./selectFromFrameworks/baseUi.js";
import {buildSuggestionButton} from "./suggestionRetriever/suggestionButton.js";
import {collectData} from "./dataCollection/dataCollector.js";
import {sendRawData} from "./sendData/dataSender.js";
import {uploadFile} from "./uploadManager/uploader.js";


const headlineAssignment = {
    "general-container": "General Information",
    "license-container": null,
    "publisher-container": "Publisher",
    "creator-container": "Creator",
    "suggestionButton-container": null,
    "educationalAlignment-container": "Educational Alignment",
    "teaches-container": "Competencies & Skills (teaches)",
    "keywords-container": "Keywords",
    "educationalLevel-container": "Educational Level"
};


export async function buildUI() {
    const container = document.getElementById('main_window');
    buildUIContainer(container);

    await storeAllToplevel();

    buildGeneralUi();
    buildLicenseUi();
    buildPublisherUi();
    buildCreatorUi();
    buildSuggestionButton();
    buildBaseUi("educationalAlignment");
    buildBaseUi("teaches");
    buildKeywordsUi();
    buildBaseUi("educationalLevel");

    buildSubmitButton(container);

    setUpUploadButton();
}


function buildUIContainer(container) {
    for (const key in headlineAssignment){
        const subContainer = document.createElement('div');
        subContainer.id = key;

        if(headlineAssignment[key]){
            const headline = document.createElement('h2');
            headline.textContent = headlineAssignment[key];
            subContainer.appendChild(headline);
        }
        container.appendChild(subContainer);
    }
}


function buildSubmitButton(container){
    const row = document.createElement('div');
    row.className = "row";

    const submitButton = document.createElement('button');
    submitButton.textContent = "Generate Metadata";
    submitButton.onclick = async function () {
        const data = collectData();
        if(data){
            await sendRawData(data);
        }
    }

    row.appendChild(submitButton);

    container.appendChild(row);
}


function setUpUploadButton() {
    const button = document.getElementById("file_upload");
    
    button.addEventListener('change', uploadFile, false);
    
}
