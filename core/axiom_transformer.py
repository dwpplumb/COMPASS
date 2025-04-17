"""
Modul zur Transformation von Axiomen zwischen verschiedenen Bezugssystemen.
"""

import logging
from core.logger_setup import setup_logger
from core.compass_engine import evaluate

# Initialisiere den Logger
logger = setup_logger(__name__, log_file='logs/compass.log')

def transform_axioms(source_axioms, target_axioms):
    """
    Transformiert Axiome vom Quell- in das Zielsystem.
    :param source_axioms: Liste von Axiomen im Quellsystem
    :param target_axioms: Liste von Axiomen im Zielsystem
    :return: Transformationsmatrix als Dictionary
    """
    transformation_matrix = {}

    for axiom in source_axioms:
        logger.info(f"Bewerte Axiom im Quellsystem: {axiom}")
        source_evaluation = evaluate({'goal': axiom})
        source_score = source_evaluation.get('connection_score', 0.0)

        logger.info(f"Bewerte Axiom im Zielsystem: {axiom}")
        target_evaluation = evaluate({'goal': axiom})
        target_score = target_evaluation.get('connection_score', 0.0)

        transformation_matrix[axiom] = {
            'source_score': source_score,
            'target_score': target_score,
            'difference': target_score - source_score
        }

    logger.info(f"Transformationsmatrix erstellt: {transformation_matrix}")
    return transformation_matrix
