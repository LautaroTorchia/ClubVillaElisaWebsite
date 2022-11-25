from src.core.board.configuration import Configuration

from src.core.db import db


def get_cfg():
    """Get configuration
    Returns:
        - Gets configuration or creates it
    """
    try:
        return db.session.query(Configuration).one()
    except:
        return add_cfg(
            Configuration(
                {
                    "record_number": 10,
                    "currency": "ARS",
                    "base_fee": 1000,
                    "due_fee": 15,
                    "payment_available": False,
                    "contact": "(0221) 487-0193",
                    "payment_header": "Recibo de Pago Villa Elisa",
                }
            )
        )


def add_cfg(cfg_data):
    """Add configuration
    Returns:
        - Added configuration
    """
    db.session.add(cfg_data)
    db.session.commit()
    return cfg_data


def update_cfg(cfg_data):
    """Update configuration
    Returns:
        - Updated configuration
    """
    db.session.query(Configuration).filter(Configuration.id == get_cfg().id).update(
        cfg_data
    )
    db.session.commit()
    return cfg_data
