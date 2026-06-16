import {buildUI} from "../buildForm.js";
import {loadGeneralData} from "./generalLoader.js";
import {loadLicenseData} from "./licenseLoader.js";
import {loadPublisherData} from "./publisherLoader.js";
import {loadAllCreatorData} from "./creatorLoader.js";
import {loadKeywordsData} from "./keywordsLoader.js";
import {loadFrameworksData} from "./frameworksDataLoader.js";
import {buildBaseUi} from "../selectFromFrameworks/baseUi.js";
import {buildKeywordsUi} from "../inputFormTemplates/keywords.js";
import {isEmpty} from "../dataCheck/checkHelper.js";


export async function loadData(inputData) {
    while(document.getElementById('main_window').children.length){
        document.getElementById('main_window').children[0].remove();
    }

    await buildUI();

    loadGeneralData(inputData);


    if(Object.keys(inputData).includes("license")){
        loadLicenseData(inputData);
    }
    if(Object.keys(inputData).includes("publisher")){
        loadPublisherData(inputData);
    }
    if(Object.keys(inputData).includes("creator")){
        loadAllCreatorData(inputData);
    }
    if(Object.keys(inputData).includes("educationalAlignment") && !isEmpty(inputData["educationalAlignment"])){
        loadFrameworksData("educationalAlignment", inputData);
    }else {
        buildBaseUi("educationalAlignment",true);
    }
    if(Object.keys(inputData).includes("teaches") && !isEmpty(inputData["teaches"])){
        loadFrameworksData("teaches", inputData);
    }else {
        buildBaseUi("teaches",true);
    }
    if(Object.keys(inputData).includes("keywords") && !isEmpty(inputData["keywords"])){
        loadKeywordsData(inputData);
    }else {
        buildKeywordsUi(true);
    }
    if(Object.keys(inputData).includes("educationalLevel") && !isEmpty(inputData["educationalLevel"])){
        loadFrameworksData("educationalLevel", inputData);
    }else {
        buildBaseUi("educationalLevel",true);
    }
}