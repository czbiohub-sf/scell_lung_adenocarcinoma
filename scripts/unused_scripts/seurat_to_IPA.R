seurat.to.ipa <- function(df, score.column, divide.by.column, gene.column, divide.append) {
  # Find appropriate columns in DE output 
  col.1 <- which(colnames(df)==divide.by.column)
  col.2 <- which(colnames(df)==score.column)
  col.3 <- which(colnames(df)==gene.column)
  # Create new table
  tab.temp <- matrix(nrow=length(unique(df[,col.3])), ncol=length(unique(df[,col.1])), 0)
  # Set colnames 
  colnames(tab.temp) <- unique(df[,col.1])
  # Set townames 
  row.names(tab.temp) <- as.character(unique(df[,col.3]))
  # Populate values 
    for(i in 1:nrow(tab.temp)){
      temp <- df[as.character(df[,col.3]) %in% row.names(tab.temp)[i] ,]
        for(j in 1:nrow(temp)){
          col.to <- which(colnames(tab.temp)==as.character(temp[j,col.1]))
          tab.temp[i,col.to] <- temp[j,col.2]
        }
    }
  # Set colnames 
  colnames(tab.temp) <- paste(divide.append, colnames(tab.temp), sep="_")
  return(tab.temp)
}
