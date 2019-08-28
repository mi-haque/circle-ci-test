import unittest
from airflow.models import DagBag
from airflow.models import Variable


class TestAtomicDag(unittest.TestCase):

    def setUp(self):
        variable = Variable()
        self.dagbag = DagBag(dag_folder=variable.get('dags_folder'))

    def test_atomic_jobs(self):
        dag_id = 'ATOMIC_JOB'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 2)

    def test_data_mart_jobs(self):
        dag_id = "DATAMART_JOB"
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 1)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAtomicDag)
unittest.TextTestRunner(verbosity=2).run(suite)
