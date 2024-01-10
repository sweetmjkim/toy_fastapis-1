class Paginations:
    def __init__(self, total_records, current_page):
        self.records_per_page = 10  # 한 페이지 당 레코드 수
        self.pages_per_block = 5  # 한 블럭 당 페이지 수

        self.total_records = total_records
        self.current_page = current_page
        self.records_per_page = 10  # 한 페이지 당 레코드 수
        self.pages_per_block = 5  # 한 블럭 당 페이지 수

        self.total_blocks = self._calculate_total_blocks()
        self.current_block = self._calculate_current_block()
        self.start_page = self._calculate_start_page()
        self.end_page = self._calculate_end_page()
        self.start_record_number = self._calculate_start_record_number()

        self.current_page_range = range(self.start_page, self.end_page + 1)
        self.previous_page = self.start_page - 1
        self.has_previous_page = self.start_page - 1 > 0
        self.next_page = self.end_page + 1
        self.has_next_page = self.current_block > self.total_blocks
        self.has_previous_block = self.current_block > 1
        self.has_next_block = self.current_block < self.total_blocks
        self.first_page = 1
        self.last_page = self.total_blocks

    def _calculate_total_blocks(self):
        return (self.total_records + self.records_per_page - 1) // self.records_per_page

    def _calculate_current_block(self):
        return (self.current_page - 1) // self.pages_per_block + 1

    def _calculate_start_page(self):
        return (self.current_block - 1) * self.pages_per_block + 1

    def _calculate_end_page(self):
        end_page = self.current_block * self.pages_per_block
        return min(end_page, self.total_blocks)
        # return end_page
    
    def _calculate_start_record_number(self):
        # 현재 페이지 번호와 페이지 당 레코드 수를 곱한 후 페이지 당 레코드 수를 빼고 1을 더하여 현재 페이지의 시작 레코드 번호를 계산
        return (self.current_page * self.records_per_page) - self.records_per_page + 1    

if __name__ == "__main__":
    # 예시 사용:
    total_records = 120  # 총 레코드 수
    # total_records = 12  # 총 레코드 수
    current_page = 1  # 현재 페이지 번호
    # current_page = 2  # 현재 페이지 번호
    current_page = 7  # 현재 페이지 번호
    current_page = 30  # 현재 페이지 번호

    pagination = Paginations(total_records, current_page)

    print(f"현재 페이지: {pagination.current_page}")
    print(f"현재 페이지 시작 레코드 번호: {pagination.start_record_number}")
    print(f"전체 블럭 페이지 수: {pagination.total_blocks}")
    print(f"현재 블럭: {pagination.current_block}")
    print(f"시작 페이지: {pagination.start_page}")
    print(f"끝 페이지: {pagination.end_page}")
    print(f"시작과 끝 페이지 리스트: {pagination.current_page_range}")
    print(f"이전 페이지 번호: {pagination.previous_page}")
    print(f"다음 페이지 번호: {pagination.next_page}")
    print(f"이전 블럭 존재 여부: {pagination.has_previous_block}")
    print(f"다음 블럭 존재 여부: {pagination.has_next_block}")
    print(f"첫 페이지 : {pagination.first_page}")
    print(f"마지막 페이지 : {pagination.last_page}")
