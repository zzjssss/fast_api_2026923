from FastAPIProject.src.demo_model.DAO.data_from_items import fake_db


def service_read_items(skip: int = 0, limit: int = 10):
    """查询所有items，skip/limit为查询参数"""
    return fake_db[skip : skip + limit]