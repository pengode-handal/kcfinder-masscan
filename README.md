# kcfinder-masscan
# Installation
```
apt-get install git
apt-get install python3
git clone https://github.com/pengode-handal/kcfinder-masscan

```

# Usage
```python
python3 scan.py [-h] [-u URL] [-l LIST] [-s SAVE] [-v]
```
## Example
### Mass Scanning: python3 <filename> -l <list filename> 
```python
python3 scan.py scan.py -l link
```
Or Save The Results
```python
python3 scan.py scan.py -l link -s result
```
### Single Scanning: python3 <filename> -u <url>
```python
python3 scan.py scan.py -u site.com
```
Or Save The Results
```python
python3 scan.py scan.py -u site.com -s result
```
