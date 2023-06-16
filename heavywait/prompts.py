
class Prompts:
    """
    This is a grab-bag of (MOOD, prompt template) tuples used by Heavywait.
    The MOOD is a workaround to deal with the temperature being a model parameter not an inference parameter.

    A separate tool was written to systematically generate and test most of these prompts. Evaluation was manual:
    If I figure out a better evaluation technique I will clean up and add to this module.
    """
    MOOD_STRICT = "strict"
    MOOD_EXPRESSIVE = "expressive"

    @staticmethod
    def get_title_prompt() -> (str,str):
        return Prompts.MOOD_EXPRESSIVE, \
               "As a clever college student, write a short title, no more than 5 words, of the following:\n\n\n\"{text}\"\n\n\nTITLE:"

    @staticmethod
    def get_keywords_prompt() -> (str, str):
        return Prompts.MOOD_STRICT,\
               "Print in CSV format the top 5 named entities, excluding numbers, found in the following text:\n\n\n\"{text}\"\n\n\nENTITIES:"

    @staticmethod
    def get_concise_summary_prompt() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE,\
               "Write a concise summary of the following:\n\n\n\"{text}\"\n\n\nSUMMARY:"

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

        print in CSV format the top one or two labels for the following text delimited by triple backticks: ```{summary}``` LABELS:
        """

    @staticmethod
    def get_links_prompt() -> (str, str):
        return Prompts.MOOD_EXPRESSIVE, """
        Find web links which are related to the text delimited by triple backticks. 
        Limit to 3 web links and output each link as markdown.

        Text:
        ```{summary}```
        """
