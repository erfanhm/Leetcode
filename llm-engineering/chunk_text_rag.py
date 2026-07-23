def chunk_text(text:str, chunk_size:int, overlap:int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError ("the chunk size should be greater than 0")
    if overlap < 0:
        raise ValueError ("The overlap should be greater than 0")
    if chunk_size <= overlap:
        raise ValueError ("The chunk size should be greater than overlap")
    words = text.split()
    if not words:
        return []
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        current_chunk = words[start:end]
        chunks.append(" ".join(current_chunk))

        if end >= len(words):
            break

        start = end - overlap

    return chunks

print(chunk_text("one two three four five six seven eight nine ten",4,1))