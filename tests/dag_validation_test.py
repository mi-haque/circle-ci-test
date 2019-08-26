import unittest
from airflow.models import DagBag
from airflow.models import Variable


class TestDagIntegrity(unittest.TestCase):
    LOAD_SECOND_THRESHOLD = 2

    def setUp(self):
        variable = Variable()
        self.dagbag = DagBag(dag_folder=variable.get('dags_folder'))

    def test_import_dags(self):
        self.assertFalse(
            len(self.dagbag.import_errors),
            'DAG import failures. Errors: {}'.format(
                self.dagbag.import_errors
            )
        )

    def test_alert_email_present(self):
        print(self.dagbag.dags.items())
        for dag_id, dag in self.dagbag.dags.items():
            print(dag_id)
            emails = dag.default_args.get('email', [])
            msg = 'Alert email not set for DAG {id}'.format(id=dag_id)
            self.assertIn('airflow@example.com', emails, msg)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDagIntegrity)
unittest.TextTestRunner(verbosity=2).run(suite)
