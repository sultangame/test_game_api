from beanie import Document, PydanticObjectId
from .crud_depends import detail_or_404
from pydantic import BaseModel


class DatabaseCRUD:
    def __init__(self, document):
        self.document: Document = document

    async def find_all(self) -> list[Document]:
        answer = await self.document.find_all().to_list()
        return answer

    async def find_one(self, _id: PydanticObjectId) -> Document | None:
        answer = await self.document.find_one({"_id": _id})
        detail = await detail_or_404(detail=answer)
        return detail

    async def find_filtered(self, filter_document: dict):
        item = await self.document.find(filter_document).to_list()
        answer = await detail_or_404(detail=item)
        return answer

    @staticmethod
    async def add_one(document: Document) -> Document:
        answer = await document.create()
        return answer

    async def delete_document(self, _id: PydanticObjectId):
        one = await self.find_one(_id=_id)
        if one:
            await one.delete()
            return {"Message": "Document was deleted"}
        return one

    async def edit_document(self, _id: PydanticObjectId, body: BaseModel):
        doc_id = _id
        des_body = body.model_dump(exclude_unset=True)
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        doc = await self.find_one(_id=doc_id)
        await doc.update(update_query)
        return doc
