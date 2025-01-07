import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.main import fine_tune_codebert, evaluate_model_performance, integrate_fine_tuned_models
from transformers import RobertaTokenizer, RobertaForMaskedLM
from datasets import Dataset

class TestFineTuneCodeBERT(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset.from_dict({"text": ["def example(): pass"]})
        self.task = "code_completion"

    def test_fine_tune_codebert(self):
        model = fine_tune_codebert(self.task, self.dataset)
        self.assertIsInstance(model, RobertaForMaskedLM)

class TestEvaluateModelPerformance(unittest.TestCase):
    def setUp(self):
        self.model = RobertaForMaskedLM.from_pretrained("microsoft/codebert-base")
        self.eval_dataset = Dataset.from_dict({"text": ["def example(): pass"], "labels": [0]})
        self.task = "code_completion"

    def test_evaluate_model_performance(self):
        metrics = evaluate_model_performance(self.model, self.eval_dataset, self.task)
        self.assertIn("accuracy", metrics)

class TestIntegrateFineTunedModels(unittest.TestCase):
    def setUp(self):
        self.models = {"code_completion": RobertaForMaskedLM.from_pretrained("microsoft/codebert-base")}
        self.pipeline = {}

    def test_integrate_fine_tuned_models(self):
        updated_pipeline = integrate_fine_tuned_models(self.models, self.pipeline)
        self.assertIn("code_completion", updated_pipeline)

if __name__ == '__main__':
    unittest.main()
