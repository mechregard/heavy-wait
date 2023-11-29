from langchain import LLMChain
from langchain import PromptTemplate
from context import TEST_RESOURCES_DIR  # noqa
from heavywait.heavywait import HeavyWait
import argparse

from heavywait.prompts import Prompts


class LabelParsing(object):

    @staticmethod
    def get_labels_prompt() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE, """
        Labels are single word topics describing some text. 
        The following labels are available to use, along with example text:
        
        'research': SOTA papers, machine learning algorithms, deep learning algorithms, statistical algorithms
        'code': software algorithms, software examples, heuristics and methods, software framework, software package, software library
        'security': security issues, hacking, injections, malware, authentication, authorization
        'mlops': mlops and devops tools or frameworks used for managing andd deploying ML models, versioning and managing data
        'analysis': notes and discussions, analysis and investigation into a speific topic

        print the top one or two labels in CSV format for the following text delimited by triple backticks: ```{text}``` LABELS:
        """

    @staticmethod
    def get_prompt() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE, """
        You are building an application based on a large language model. Your task is to create
        a prompt for identifying descriptive labels for a piece of text. You will also limit
        the possible labels to the following (short description follows each label):

        'algo': software algorithms, software examples, heuristics and methods 
        'devops': devops techniques such as building or deploying software or infrastructure, CI/CD, K8S
        'mlops': mlops tools or frameworks used for managing andd deploying ML models, versioning and managing data
        'frameworks': software framework, software package, software library

        {text}:
        """

    @staticmethod
    def get_c1() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE, """
What is the genre/category of the following text delimited by triple backticks? 
Assign one or more appropriate categories/genres using the following:
 
'research': for SOTA papers, machine learning algorithms, deep learning algorithms, statistical algorithms
'code': for software algorithms, software examples, heuristics and methods, software framework, software package, software library
'security': for security issues, hacking, injections, malware, authentication, authorization
'mlops': for mlops and devops tools or frameworks used for managing andd deploying ML models, versioning and managing data
'analysis': for notes and discussions, analysis and investigation into a specific topic

 ```{text}```
"""

    @staticmethod
    def get_strict() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE, """
The following text delimited by triple backticks is a blog post
```{text}```
Select one or two labels which best categorize the blog post and output as CSV.
The labels you select must exist in the following list:
['research','code','security','mlops','algorithms','links','analysis','planning','ideas']
"""

    def parse_output(self, markdown: str):
        hw = HeavyWait()
        llm = hw.llm_map[LabelParsing.get_strict()[0]]
        prompt = PromptTemplate.from_template(LabelParsing.get_strict()[1])
        chain = LLMChain(llm=llm, prompt=prompt, output_key="labels")
        input = [{"text": markdown}]
        print(chain.generate(input))


if __name__ == '__main__':
    """
    Manually test different prompts and outputs for label generation
    Run:
      python tests/test_labels.py
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--markdown",
        type=str,
        default=TEST_RESOURCES_DIR+"/src/efficient-transformers.md",
        help="markdown")
    CARGS = parser.parse_args()
    with open(CARGS.markdown) as f:
        content = f.read()
    LabelParsing().parse_output(content)