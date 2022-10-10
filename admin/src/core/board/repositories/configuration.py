from src.core.board.configuration import Configuration

from src.core.db import db
# begin config repo
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
                    "record_number": 6,
                    "ord_criteria": "ALPH",
                    "currency": "ARS",
                    "base_fee": 100,
                    "due_fee": 50,
                    "payment_available": True,
                    "contact": "villa elisa",
                    "payment_header": "pagos",
                }
            )
        )
    # TODO discuss default values


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
    cfg = get_cfg()
    cfg.record_number = cfg_data.record_number
    cfg.ord_criteria = cfg_data.ord_criteria
    cfg.currency = cfg_data.currency
    cfg.base_fee = cfg_data.base_fee
    cfg.due_fee = cfg_data.due_fee
    cfg.payment_available = cfg_data.payment_available
    cfg.contact = cfg_data.contact
    cfg.payment_header = cfg_data.payment_header

    # TODO change this
    db.session.commit()
    return cfg_data


# end config repo
