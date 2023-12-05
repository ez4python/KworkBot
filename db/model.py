from sqlalchemy import BIGINT, CheckConstraint, create_engine, TEXT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.config import AbstractClass, Config


class Customer(AbstractClass):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)
    lang: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(default="CUSTOMER")
    tasks: Mapped[list['Task']] = relationship(back_populates='customer')


class Category(AbstractClass):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column()
    tasks: Mapped[list['Task']] = relationship(back_populates="category")


#
class Task(AbstractClass):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    title: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(TEXT)
    status: Mapped[str] = mapped_column(default="PROCESSING")
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped['Category'] = relationship(back_populates="tasks")
    customer: Mapped['Customer'] = relationship(back_populates="tasks")

#
# class Specialty(AbstractClass):
#     pass
