# TODO: complete this class

class PaginationHelper:

# The constructor takes in an array of items and a integer indicating
# how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection_len = len(collection)
        self.items_per_page = items_per_page        
# returns the number of items within the entire collection
    def item_count(self):
        return self.collection_len

  
# returns the number of pages
    def page_count(self):
        if self.collection_len%self.items_per_page < self.items_per_page:
            self.page_count  = self.collection_len//self.items_per_page + 1
            return self.page_count   

	
# returns the number of items on the current page. page_index is zero based
# this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > (self.page_count - 1):
            return -1
        elif self.collection_len <= self.items_per_page:
            new_page_index = self.collection_len
            return self.collection_len
        elif page_index == (self.collection_len//self.items_per_page) - 1:
            new_page_index = self.items_per_page
            return new_page_index
        else:
            new_page_index = self.collection_len - (page_index * self.items_per_page)
            return new_page_index
            
  
# determines what page an item is on. Zero based indexes.
# this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > self.collection_len - 1 or item_index < 0:
            return -1
        else:
            new_page_index = (item_index)//self.items_per_page
            return  new_page_index

if __name__ == '__main__':
    collection = range(1,25)
    helper = PaginationHelper(collection, 10)
    print(helper.item_count())
    print(helper.page_count())
    print(helper.page_item_count(2))
    print(helper.page_index(-23))
    
