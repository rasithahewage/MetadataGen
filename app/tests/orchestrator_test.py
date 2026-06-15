from app.suggestion_management.suggestion_manager import generate_full_suggestion
from app.metadatabuilder.build_full_metadata import build_metadata
#from pprint import pprint
import json

title = "Sustainability in the Digital Age: Efficient AI Techniques in the LLM Era"
description = """
    <h2>Welcome to the \"Sustainability in the Digital Age\" series</h2>\\n\\n<p>In an era where "
    digital technologies are reshaping industries and daily life, the environmental impact of AI systems has 
    become a growing concern. This course explores efficient AI methodologies to address these challenges. From 
    deep learning model compression to low-bit quantization and collaborative inference, we delve into techniques 
    that enhance computational efficiency and reduce energy consumption. In Week 2, we focus on low-bit 
    quantization specifically for large language models (LLMs), showcasing cutting-edge open-source tools and 
    models. Join us to learn how to build sustainable AI systems while pushing the boundaries of innovation. 
    </p>\\n\\n<hr>\\n\\n<p>This course is part of the <strong>Sustainability in the Digital Age</strong> series, 
    a collaborative project between colleagues from Stanford University, SAP and the Hasso Plattner Institute. </p>\\n
    """
publisher = {
    "name": "openHPI",
    "url": "https://open.hpi.de",
    "description": "openHPI is the digital education platform of the Hasso Plattner Institute, Potsdam, Germany. " +
                   "On openHPI you take part in a worldwide social learning network based on interactive online " +
                   "courses covering different subjects in Information and Communication Technology (ICT)."
}
creator = [
    {
            "name": "Haojin Yang",
            "honorificPrefix": None,
            "description": "PD Dr. Haojin Yang is a senior researcher and multimedia and machine learning (MML) " +
            "research group leader at Hasso-Plattner-Institute (HPI). Since 2019, he has been habilitated for a " +
            "professorship. His research focuses on efficient deep learning, model acceleration and compression, " +
            "and AI agentic systems.",
            "type": "Person"
    },
]

course_license = [
    {
        "identifier": "CC-BY-NC-SA-4.0",
        "url": "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html"
    }
]

raw_data = {
    "name": title,
    "description": description,
    "publisher": publisher,
    "creator": creator,
    "url": "https://open.hpi.de/courses/aimethods2025",
    "license": course_license,
    "teaches": "ESCO",
    "educationalAlignment": "ISCED-F",
    "educationalLevel": "DigComp",
    "keywords": None
}

#pprint(generate_suggestion(raw_data))

llm_suggestion = {
    'educationalLevel': {
        'description': 'autonomous user, can solve straightforward problems',
        'conceptUrl': 'https://metadata-generator.xikolo.de/framework/digcomp/3',
        'educationalFramework': 'DigComp'
    },
    'keywords': [
        'AI',
        'Sustainability',
        'Digital Age',
        'LLM',
        'Energy Consumption',
        'Deep Learning',
        'Model Compression',
        'Quantization',
        'Computational Efficiency',
        'Open-source Tools'
    ]
}


with open("test_output_full.json", 'w') as f:
    f.write(json.dumps(generate_full_suggestion(raw_data), indent=4))

