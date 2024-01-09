import math

class Paginations:
    def __init__(self, totalCount, currentPage):
        self.pageScale = 10     # 페이지당 게시물 수
        self.blockScale = 5     # 블록당 페이지수
        self.currentPage = currentPage # 현재 페이지 번호
        self.previousPage = 0   # 이전 페이지
        self.nextPage = 0       # 다음 페이지
        self.totalPage = 0      # 전체 페이지 갯수
        self.currentBlock = 0   # 현재 페이지 블록 번호
        self.totalBlock = 0     # 전체 페이지 블록 갯수
        self.pageBegin = 0      # 페이지 내에서의 레코드 시작 번호
        self.pageEnd = 0        # 페이지 내에서의 레코드 마지막 번호
        self.blockStart = 0     # 페이지 블록 내에서의 시작 페이지 번호
        self.blockEnd = 0       # 페이지 블록 내에서의 마지막 페이지 번호
        self.totalCount = totalCount  # 페이지 블록 내에서의 마지막 페이지 번호
        
        self.setTotalPage(totalCount)
        self.setPageRange()
        self.setTotalBlock()
        self.setBlockRange()

        self.page_range = range(self.pageBegin, self.pageEnd+1)
        
    def setTotalBlock(self):
        self.totalBlock = math.ceil(self.totalPage / self.blockScale)

    def setBlockRange(self):
        self.currentBlock = math.ceil((self.currentPage - 1) / self.blockScale) + 1
        self.blockStart = (self.currentBlock - 1) * self.blockScale + 1
        self.blockEnd = self.blockStart + self.blockScale - 1

        if self.blockEnd > self.totalPage:
            self.blockEnd = self.totalPage

        self.previousPage = 1 if self.currentBlock == 1 else (self.currentBlock - 1) * self.blockScale
        self.nextPage = self.totalPage if self.currentBlock > self.totalBlock else (self.currentBlock * self.blockScale) + 1

        if self.nextPage >= self.totalPage:
            self.nextPage = self.totalPage

    def setPageRange(self):
        self.pageBegin = (self.currentPage - 1) * self.pageScale
        self.pageEnd = self.pageBegin + self.pageScale - 1

    def setTotalPage(self, totalCount):
        self.totalPage = math.ceil(totalCount * 1.0 / self.pageScale)
